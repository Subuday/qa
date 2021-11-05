package com.kpi.qa1client;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.json.JSONObject;

import java.io.FileWriter;
import java.io.IOException;
import java.util.zip.CRC32;
import java.util.zip.Checksum;

//docker build -t subuday/qa1client .
//docker run -d --rm -e PORT=8080 --net lab1 --name client --mount type=volume,source=clientvol,destination=/usr/src/app/clientdata subuday/qa1client
//docker exec -it <container> /bin/bash

public class Application {

    public static void main(String[] args) throws InterruptedException {
        String port = System.getenv("PORT");
        if (port == null) {
            port = "8080";
        }
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url("http://server:" + port + "/hello").build();
        try (Response response = client.newCall(request).execute()) {
            JSONObject jsonObject = new JSONObject(response.body().string());
            String data = jsonObject.getString("data");
            long checksum = jsonObject.getLong("checksum");
            long dataChecksum = getCRC32Checksum(data.getBytes());
            if (checksum == dataChecksum) {
                try (FileWriter writer = new FileWriter("./clientdata/data.txt")) {
                    writer.write(data);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        Thread.sleep(10_000_000);
    }

    public static long getCRC32Checksum(byte[] bytes) {
        Checksum crc32 = new CRC32();
        crc32.update(bytes, 0, bytes.length);
        return crc32.getValue();
    }
}
