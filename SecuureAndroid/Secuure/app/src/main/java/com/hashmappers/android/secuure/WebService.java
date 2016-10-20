package com.hashmappers.android.secuure;


/**
 * Created by voidtm on 10/20/16.
 * non functional purpose
 * Based off of http://wiki.workassis.com/android-retrofit-2-1-http-client/
 */


import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.Retrofit;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


public class WebService {
    // Attempt to access the web
    public static final String BASE_URL = "http://api.myservice.com/";
    private static WebInterface service;

    public static WebInterface WebService() {

        Gson gson = new GsonBuilder()
                .setDateFormat("yyyy-MM-dd'T'HH:mm:ssZ")
                .create();

        Retrofit rest = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create(gson))
                .build();
        ;

        service = rest.create(WebInterface.class);
        return service;
    }
}
