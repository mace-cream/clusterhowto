How to start the server
```
cd /home/feng/LanguageTool # on storage node
nohup java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8088 --allow-origin "*" --public --languageModel ./ > run.log 2>&1 &
```

Use `kill id` to stop the service.