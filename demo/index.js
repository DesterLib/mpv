const path = require("path");
const { BrowserWindow, app } = require("electron");
const { getPluginEntry } = require("../index");

const pdir = path.join(__dirname, "..", "build", "Release");
if (process.platform !== "linux") {
  process.chdir(pdir);
}
app.commandLine.appendSwitch("no-sandbox");
app.commandLine.appendSwitch("ignore-gpu-blacklist");
app.commandLine.appendSwitch("register-pepper-plugins", getPluginEntry(pdir));

app.on("ready", () => {
  const win = new BrowserWindow({
    width: 1280,
    height: 720,
    useContentSize: process.platform !== "linux",
    title: "Dester mpv video plugin",
    webPreferences: { plugins: true },
  });
  win.loadURL(`file://${__dirname}/index.html`);
});

app.on("window-all-closed", () => {
  app.quit();
});
