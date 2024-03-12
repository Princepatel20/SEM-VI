package com.example.pr4;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    EditText e1,e2,e3,e4,e5,e6;
    Button b1,b2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        e1=findViewById(R.id.Name);
        e2=findViewById(R.id.Email);
        e3=findViewById(R.id.Password);
        e4=findViewById(R.id.PhoneNo);
        e5=findViewById(R.id.Date);

        b1=findViewById(R.id.Submit);
        b2=findViewById(R.id.Reset);

        b1.setOnClickListener(new view.clickListener() {
                @Override
                public void onclick(view view) {
                   Intent i=new Intent(MainActivity.this, Login.class);
                   startActivity(i);
        }
        });
    }
}