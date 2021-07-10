Megaglest is an online strategy game. We have deployed it on our server. Normally it is not started.
To start it, at storage node terminal, go to `/home/feng/megaglest-3.13.0/` and run `./start_megaglest_gameserver --headless-server-mode=exit`.

Then from client game ( windows binary can be downloaded by `scp username@10.8.6.22:/home/feng/Downloads/MegaGlest-Installer-3.13.0_windows_64bit.exe ./`)
choose Network LAN mode and enter `10.8.6.21`.

Notice: use `wget github_game_release_url` on the server cluster to download the binary for other platforms.