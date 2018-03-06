package com.example.jersey;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.example.model.Activity;
import com.example.repository.ActivityRepository;
import com.example.repository.ActivityRepositoryStub;

import java.util.List;

@Path("activities")
public class ActivityResource {

    private ActivityRepository activityRepository = new ActivityRepositoryStub();

    @GET
    @Produces(MediaType.APPLICATION_XML)
    public List<Activity> getAllActivities() {
        return activityRepository.findAllActivities();
    }
}
