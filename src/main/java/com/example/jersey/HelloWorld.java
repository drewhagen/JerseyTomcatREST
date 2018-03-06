package com.example.jersey;

//import javax.ws.rs.ApplicationPath;
//import javax.ws.rs.core.Application;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

/**
 * @author: Drew Hagen
 * @link: https://medium.com/@jamsesso/starting-out-with-jersey-apache-tomcat-using-intellij-6338d93ffd40
 * @link: https://stackoverflow.com/questions/42788015/http-404-with-java-maven-jersey2-tomcat-8-5-and-intellij-idea
 * */
@Path("hello")
public class HelloWorld {
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getMessage() {
        return "Hello world!";
    }
}
