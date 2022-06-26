{
    "targets": [
        {
            "target_name": "mpvjs",
            "win_delay_load_hook": "false",
            "sources": ["index.cc"],
            "conditions": [
                ["OS=='win'", {
                    "include_dirs": ["libraries/win/include"],
                    "libraries": ["-llibmpv.dll.a", "-lppapi_cpp", "-lppapi_gles2"],
                    "library_dirs": [
                        "libraries/win/host",
                        "libraries/win/mpv",
                    ],
                }, "OS=='linux'", {
                    "include_dirs": ["libraries/linux/include"],
                    "libraries": ["-lmpv"],
                    "library_dirs": ["libraries/linux/host"],
                    "ldflags": ["-static-libstdc++"],
                }],
            ],
        },
    ],
}
