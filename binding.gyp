{
    "targets": [
        {
            "target_name": "mpv",
            "win_delay_load_hook": "false",
            "sources": ["index.cc"],
            "include_dirs": ["libraries/include"],
            "conditions": [
                ["OS=='win'", {
                    "libraries": ["-llibmpv.dll.a", "-lppapi_cpp", "-lppapi_gles2"],
                    "library_dirs": [
                        "libraries/win/host",
                        "libraries/win/mpv",
                    ],
                }, "OS=='linux'", {
                    "libraries": ["-lmpv"],
                    "library_dirs": ["libraries/linux/host"],
                    "ldflags": ["-static-libstdc++"],
                }, "OS=='mac'", {
                    "libraries": ["-lmpv"],
                    "library_dirs": [
                        "libraries/mac/host",
                        "libraries/mac/mpv",
                    ],
                    "xcode_settings": {"MACOSX_DEPLOYMENT_TARGET": "10.9"},
                }],
            ],
        },
    ],
}
