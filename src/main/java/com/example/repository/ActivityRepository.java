package com.example.repository;

import com.example.model.Activity;

import java.util.List;

public interface ActivityRepository {

    List<Activity> findAllActivities();

}
