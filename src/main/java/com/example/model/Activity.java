package com.example.model;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class Activity {

    private String description;
    private int duration;

    public String getDescription(){
        return this.description;
    }
    public void setDescription(String description) {
        this.description = description;
    }
    public int getDuration(){
        return this.duration;
    }
    public void setDuration(int duration) {
        this.duration = duration;
    }
}
