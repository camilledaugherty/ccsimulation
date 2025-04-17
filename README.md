# ccsimulation
Steps on how to run congestion control experiments using Mahimahi and Pantheon:
1. Install Oracle VirtualBox
2. Install Ubuntu 16.04 ISO
3. Create a new virtual machine within VirtualBox using the Ubuntu ISO previously installed.
4. Open up a terminal and create a directory to hold your project files.
5. Run the command `git clone https://github.com/StanfordSNR/pantheon.git` to clone the Pantheon repository on your VM.
6. Enter the pantheon folder that is created and run the command `tools/fetch_submodules.sh` to update the third party modules.
7. Run the command `tools/install_deps.sh` to install globally required dependencies.
8. Now moving to Mahimahi, install the list of dependencies required (located on mahimahi.mit.edu) using sudo. Note: install apache2-dev along with apache2-bin!
9. Go to src/wrappers from within the pantheon directory, where we will be building mahimahi from source.
10. Run these commands in root to install Mahimahi:
      ```
      $ git clone https://github.com/ravinet/mahimahi
      $ cd mahimahi
      $ ./autogen.sh
      $ ./configure
      $ make
      $ sudo make install
      ```
12. Returning to Pantheon, choose 3 congestion control schemes you want to test on your emulated network. The full list can be found within the src/wrappers directory of Pantheon.
13. Once you have decided, return to the pantheon directory and run `src/experiments/setup.py --install-deps --schemes "<scheme1> <scheme2> <scheme3>"`, replacing the <scheme> with your chosen schemes. Install additional dependencies as errors arise.
14. To set up the congestion control schemes, run `src/experiments/setup.py --setup --schemes "<scheme1> <scheme2> <scheme3>"`.
15. To create the trace files, use the custom script gen_trace.py. From the src/experiments directory, run `python gen_trace.py <uplink/downlink> <duration> > <tracefile_name.trace>` to pipe the correct integers for your requested mbps and length into a trace file.
16. To test the schemes with your requested bandwidth and delay, run this command from the pantheon directory: `src/experiments/test.py local --runtime <runtime> --schemes "<scheme1> <scheme2> <scheme3>" --uplink-trace src/experiments/<tracefile>.trace --downlink-trace src/experiments/<tracefile>.trace --append-mm-cmds "mm-delay <delay>"`
17. After each experiment, run `src/analysis/analyze.py` to automatically create a report and graphs for each congestion control scheme.


***If any files or directories give you trouble with reading or writing, enter sudo and run `sudo chown <username> <file/dir>`
