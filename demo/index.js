const { BrowserWindow, app } = require('electron');
const path = require('path');

const pluginDir = path.join(__dirname, '..', 'build', 'Release');
if (process.platform !== 'linux') process.chdir(pluginDir);

const getPluginEntry = (pluginDir, pluginName = 'mpv.node') => {
    const containsNonASCII = (str) => {
        for (let i = 0; i < str.length; i++) {
            if (str.charCodeAt(i) > 255) {
                return true;
            }
        }
        return false;
    };
    const PLUGIN_MIME_TYPE = 'application/x-mpv';

    const fullPluginPath = path.join(pluginDir, pluginName);
    let pluginPath = path.relative(process.cwd(), fullPluginPath);
    if (path.dirname(pluginPath) === '.') {
        if (process.platform === 'linux') {
            pluginPath = `.${path.sep}${pluginPath}`;
        }
    } else {
        if (process.platform === 'win32') {
            pluginPath = fullPluginPath;
        }
    }
    if (containsNonASCII(pluginPath)) {
        if (containsNonASCII(fullPluginPath)) {
            throw new Error('Non-ASCII plugin path is not supported');
        } else {
            pluginPath = fullPluginPath;
        }
    }
    return `${pluginPath};${PLUGIN_MIME_TYPE}`;
};

app.commandLine.appendSwitch('no-sandbox');
app.commandLine.appendSwitch('ignore-gpu-blacklist');
app.commandLine.appendSwitch('register-pepper-plugins', getPluginEntry(pluginDir));

app.on('ready', () => {
    const win = new BrowserWindow({
        width: 1280,
        height: 720,
        useContentSize: process.platform !== 'linux',
        title: 'Dester mpv plugin',
        webPreferences: { plugins: true },
    });
    win.loadURL(`file://${__dirname}/index.html`);
});

app.on('window-all-closed', () => {
    app.quit();
});
