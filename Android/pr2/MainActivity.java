MainActivity.java
package com.example.pr2;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.d("Create", "Activity created");
    }
    @Override
    protected void onStart() {
        super.onStart();
        Log.d("Start", "Activity Started");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d("Pause", "Activity Resume");
    }
    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d("Restart", "Activity Restarted");
    }
    @Override
    protected void onResume() {
        super.onResume();
        Log.d("Resume", "Activity Resumed");
    }
    @Override
    protected void onStop() {
        super.onStop();
        Log.d("Stop", "Activity Stopped");
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d("Destroy", "Activity Destroyed");
    }
}
