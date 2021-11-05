package com.kpi.qaassigment1;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.zip.CRC32;
import java.util.zip.Checksum;

//docker network create lab1
//docker build -t subuday/qaassigment1 .
//docker run -d --rm -e PORT=8080 --network lab1 --name server -p 8080:8080 --mount type=volume,source=servervol,destination=/usr/src/app/serverdata subuday/qaassigment1

@SpringBootApplication
@RestController
public class Application {

    public static void main(String[] args) {
        createServerData();
        SpringApplication app = new SpringApplication(Application.class);
        String port = System.getenv("PORT");
        if (port == null) {
            port = "8080";
        }
        app.setDefaultProperties(Collections.singletonMap("server.port", port));
        app.run(args);
    }

    @GetMapping("/hello")
    public String hello() {
        try {
            String data = new String(Files.readAllBytes(Paths.get("./serverdata/random.txt")));
            long checksum = getCRC32Checksum(data.getBytes());

            ObjectMapper objectMapper = new ObjectMapper();
            ObjectNode root = objectMapper.createObjectNode();
            root.put("data", data);
            root.put("checksum", checksum);

            return objectMapper.writeValueAsString(root);
        } catch (IOException e) {
            return "Error";
        }
    }

    private static void createServerData() {
        File file = new File("./serverdata/random.txt");
        try {
            if (file.createNewFile()) {
                try (FileOutputStream fos = new FileOutputStream(file)) {
                    for (int i = 0; i < 1024; i++) {
                        char c = (char) ((int) (Math.random() * 1000) % 26 + 97);
                        fos.write(c);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static long getCRC32Checksum(byte[] bytes) {
        Checksum crc32 = new CRC32();
        crc32.update(bytes, 0, bytes.length);
        return crc32.getValue();
    }
}
