package com.unittest.android.phpunittest;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;

/**
 * Created by voidtm on 11/23/16.
 */

public interface WebInterface {
    // All calls use POST due the way server is set up and requested input.
    @Multipart
    @POST("read_mysql_android.php")
    Call<JsonArray> getAllAccounts(@Part("arg_usr")String usr, @Part("arg_pwd") String pwd);

    @Multipart
    @POST("delete_mysql_android.php")
    Call<String> deleteAccount(@Part("arg_usr") String usr, @Part("arg_pwd") String pwd,
                               @Part("arg_del_acc") String acc, @Part("arg_del_ws") String name);

    @Multipart
    @POST("edit_mysql_android.php")
    Call<String> editAccount(@Part("arg_usr") String usr, @Part("arg_pwd") String pwd,
                             @Part("arg_edit_acc") String accUsr, @Part("arg_edit_ws") String name,
                             @Part("arg_edit_pwd") String accPwd, @Part("arg_edit_note") String note);

    @Multipart
    @POST("register_mysql_android.php")
    Call<String> registerUser(@Part("arg_usr") String username, @Part("arg_pwd") String password,
                              @Part("arg_fname") String fname, @Part("arg_lname") String lname);

    @Multipart
    @POST("insert_mysql_android.php")
    Call<String> addAccount(@Part("arg_usr") String usr, @Part("arg_pwd") String pwd,
                            @Part("arg_add_acc") String accUsr, @Part("arg_add_ws") String name,
                            @Part("arg_add_pwd") String accPwd, @Part("arg_add_note") String note);

    @Multipart
    @POST("login_mysql_android.php")
    Call<JsonObject> login(@Part("arg_usr") String username, @Part("arg_pwd") String password);

}