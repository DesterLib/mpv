{
    "targets": [
        {
            "target_name": "mpvjs",
            "win_delay_load_hook": "false",
            "sources": ["index.cc"],
            "libraries": ["-lppapi_cpp", "-lppapi_gles2"],
            "conditions": [
                ["OS=='win'", {
                    "include_dirs": ["libraries/nacl/pepper_49/include", "libraries/libmpv/include"],
                    "libraries": ["-llibmpv.dll.a"],
                    "conditions": [
                        ["target_arch=='ia32'", {
                            "library_dirs": [
                                "libraries/nacl/pepper_49/lib/win_x86_32_host/Release",
                                "libraries/libmpv",
                            ],
                        }, "target_arch=='x64'", {
                            "library_dirs": [
                                "libraries/nacl/pepper_49/lib/win_x86_64_host/Release",
                                "libraries/libmpv",
                            ],
                        }],
                    ],
                }, {
                    "include_dirs": ["libraries/nacl/pepper_49/include"],
                    "libraries": ["-lmpv"],
                    "conditions": [
                        ["OS=='linux'", {
                            "defines": ["_GLIBCXX_USE_CXX11_ABI=0"],
                            "library_dirs": ["libraries/nacl/pepper_49/lib/linux_host/Release"],
                            "ldflags": ["-static-libstdc++"],
                        }, "OS=='mac'", {
                            "xcode_settings": {"MACOSX_DEPLOYMENT_TARGET": "10.9"},
                            "library_dirs": ["libraries/nacl/pepper_49/lib/mac_host/Release"],
                        }],
                    ],
                }],
            ],
        },
    ],
}
