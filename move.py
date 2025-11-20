mvn archetype:generate -DgroupId=com.example.demo \
-DartifactId=SampleProject \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example.demo</groupId>
    <artifactId>SampleProject</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <!-- Gson JSON Library -->
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.10.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Plugin to run Java using Maven -->
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <mainClass>com.example.demo.App</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
APp.java
package com.example.demo;

import com.google.gson.Gson;

public class App {
    public static void main(String[] args) {
        Gson gson = new Gson();

        Person p = new Person("Srika", 24);
        String jsonData = gson.toJson(p);

        System.out.println("Converted to JSON: " + jsonData);
    }
}

class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
cd SampleProject
mvn package
mvn exec:java
