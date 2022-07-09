   package com.example.whatsaver;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import android.os.Bundle;
import android.os.Handler;
import android.widget.Toast;

import java.io.File;
import java.util.ArrayList;

   public class MainActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    SwipeRefreshLayout swipeRefreshLayout;

    StoryAdapter storyAdapter;
    File[] files;
    ArrayList<Object> fileList = new ArrayLists<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initViews();

    }

    private void initViews() {
        recyclerView = findViewById(R.id.recycler_view);
        swipeRefreshLayout = findViewById(R.id.swipeRecyclerview);

        SwipeRefreshLayout.setOnRefreshListener(new SwipeRefreshLayout(.OnRefreshListener() {
            @Override
            public void onRefresh() {
                swipeRefreshLayout.setRefreshing(true);
                setUpRefreshLayout();
                (
                   new Handler() ).postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        swipeRefreshLayout.setRefreshing(false);
                        Toast.makeText(MainActivity.this, "", Toast.LENGTH_SHORT).show();
                    }
                });


            }
        });

        }

       private void setUpRefreshLayout() {
        fileList.clear();
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager( this));
        storyAdapter = new StoryAdapter( context MainActivity.this.getData());
        recyclerView.setAdapter(storyAdapter);
        storyAdapter.notifyDataSetChanged();

       }

       private ArrayList<object> getData() {

   }
}