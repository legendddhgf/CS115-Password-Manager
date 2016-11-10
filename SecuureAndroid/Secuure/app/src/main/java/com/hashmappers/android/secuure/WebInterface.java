package com.hashmappers.android.secuure;

/**
 * Created by voidtm on 10/20/16.
 * Get php files from ios-app
 */

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import java.util.List;
import okhttp3.ResponseBody;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.Field;
import retrofit2.http.GET;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;
import retrofit2.http.Path;
import retrofit2.http.Query;


public interface WebInterface {

    // note for get we should be using query strings instead
    @Multipart
    @POST("read_mysql.php")
    Call<JsonArray> getAllAccounts(@Part("arg_usr")String usr, @Part("arg_pwd") String pwd);

    @Multipart
    @DELETE("delete_mysql.php")
    Call<User> deleteAcc(@Part("arg_usr") String usr, @Part("arg_pwd") String pwd,
                         @Part("arg_del_acc") String acc, @Part("arg_del_ws") String name);


    @Multipart
    @POST("register_mysql.php")
    Call<String> registerUser(@Part("arg_usr") String username, @Part("arg_pwd") String password,
                               @Part("arg_fname") String fname, @Part("arg_lname") String lname);

    @Multipart
    @POST("insert_mysql.php")
    Call<Boolean> addAccount(@Part("arg_usr") String usr, @Part("arg_pwd") String pwd,
                             @Part("arg_add_acc") String accUsr, @Part("arg_add_ws") String name,
                             @Part("arg_add_pwd") String accPwd, @Part("arg_add_note") String note);

    @Multipart
    @POST("login_mysql.php")
    Call<JsonObject> login(@Part("arg_usr") String username, @Part("arg_pwd") String password);

}

