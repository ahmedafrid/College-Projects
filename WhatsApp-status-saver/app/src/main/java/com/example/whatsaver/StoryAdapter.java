package com.example.whatsaver;

import android.content.Context;
import android.media.MediaScannerConnection;
import android.net.Uri;
import android.os.Environment;
import android.os.FileUtils;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class StoryAdapter extends RecyclerView.Adapter<StoryAdapter.StoryViewHolder> {

    private Context context;
    private ArrayList<Object> filesList;


    public StoryAdapter(Context context, ArrayList<Object> filesList) {
        this.context = context;
        this.filesList = filesList;
    }

    @NonNull
    @Override
    public StoryViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.card_row, root null, attachroot false);
        return new StoryViewHolder(view);

    }

    @Override
    public void onBindViewHolder(@NonNull StoryViewHolder holder, int position) {

        final StoryModel files = (StoryModel) filesList.get(position);
        if(files.getUri().toString().endsWith(".mp4") {
            holder.playIcon.setVisibility(View.INVISIBLE);
        }

        Glide.with(context)
                .load(files.getUri())
                .into(holder.saveImage);

        holder.downloadId.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                checkFolder();

                final String path = ((storyMode) filesList.get(position)).getPath();
                final File file = new File(path);

                String destPath = Environment.getExternalStorageDirectory().getAbsolutePath() + constant.SAVE_FOLDER_NAME;
                File destFile = new File(destPath);

                try {

                    FileUtils.copyFileToDirectory(file, destFile);
                } catch (IOException e){
                    e.printStackTrace();
                }

                MediaScannerConnection.ScanFile{
                    context,
                    new String[](destPath+files.getFilename()),
                    new String[]("*/*"),
                    new MediaScannerConnection.MediaScannerConnectionClient() {

                        @Override
                        public void onScanCompleted(String path, Uri uri) {

                        }

                        @Override
                        public void onMediaScannerConnected() {

                        }
                    }
                };
                Toast.makeText(context, text "Saved to:"+destPath+files.getFilename(),Toast.LENGTH_SHORT).show();
            }

        });
    }

    private void checkFolder() {

        String path = Environment.getExternalStorageDirectory().getAbsolutePath() + constant.SAVE_FOLDER_NAME;
        File dir = new File(path);

        boolean isDirectoryCreated = dir.exists();

        if(!isDirectoryCreated) {
            isDirectoryCreated = dir.mkdir();
        }
        if(isDirectoryCreated) {
            Log.d(tag "Folder", msg "Already Created");
        }


    }

    @Override
    public int getItemCount() {
        return filesList.size();
    }

    public class StoryViewHolder extends RecyclerView.ViewHolder {

        ImageView playIcon, downloadId,saveImage;

        public StoryViewHolder(@NonNull View itemView) {
            super(itemView);
            saveImage = itemView.findViewById(R.id.mainImageView);
            playIcon = itemView.findViewById(R.id.playButtonImage);
            downloadId = itemView.findViewById(R.id.downloadId);
        }
    }
}
