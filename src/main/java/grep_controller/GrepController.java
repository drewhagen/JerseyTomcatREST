package grep_controller;

import java.lang.ProcessBuilder;

/**
 * Created by Drew on 2/27/18.
 */
public class GrepController {

    private boolean isWindows = System.getProperty("os.name")
            .toLowerCase().startsWith("windows");

    public void runGrep(String repoPath, String keyword, String csvOutPath) throws Exception{
        ProcessBuilder builder = new ProcessBuilder();
        if(isWindows) {
            builder.command("cmd.exe", "/c",
                    "start \"\" \"%PROGRAMFILES%\\Git\\bin\\sh.exe\" --login", "ls");
        }
        else {
            builder.command("sh", "-c", "ls");
        }
        builder.command("cd "+repoPath, "grep -Hrin "+keyword+" >> "+csvOutPath);
        //needs a waitFor() or something to verify completion.
    }

}