The edited files are:

run_attack.py
loss.py
attacks/pgd.py
attacks/attack.py
utils.py

The added files are:
test.py
apgd.py
plot_results_per_epoch.py

In run_attack.py there are two options or runnig. 
One of them is to run the application through the test.py file, and the other one is to run it through run_attack.py iteslf.
The last one is used for the last train (for creating the final perturvation), and it's used all the data for training, without using any separated test or eval data (the eval data will be the same as the train data).
In this option, the configuration parameters should be passed through the command line.
The first option is used for parameters choosing.
The test.py file is used for configuration definition, and call the test function of run_attack.py.
This function has two options. If the flag of cross_validation is activated, it runs a cross validation as explained in the report file.
Otherwise, it defines the folder 0 to be the test folder, a different random folder to be the eval folder, and all the rest to be the train folders.
When running through the test.py file, there is no need to send any parameter through the command line.

The loss.py file contains all the modification of the original loss function, without changing the method signature.

The perturb function of attack.py file was edited to have more parameters for the test.

The pgd.py file contains all the modification of the original pgd function, without changing the method signature, except the additional parameters for the test.

The utils.py file contains all the additional parameters, and modified to the new parameters.

The apgd.py contains the implementation of the apgd optimizer.

The plot_results_per_epoch.py file is used to create the experiment graphs according to the data that saved in the result/loss_lists folder.

To reproduce the resulds of the test, the data folder should be inside the src folder, and the test.py file should be modified to the relevant configuration, and run through the command line without parameters.

After running the test.py file, the plot_results_per_epoch.py will be able to show the graphs.
