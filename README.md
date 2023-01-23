
# Countries API with Pytest

The readmy describes about the solution implemented and the means to run it.

### Problem Description

Description
Using PyTest framework create test cases for 6 countries (2 from Asia, 2 from Europe
and 2 from Africa ) from  https://restcountries.com/v3.1/all .

What is expected?

•  There should be an option to execute the tests from the different continents
separately.

• The test data should be taken from a csv file.

### Solution

#### • The framework is pytest.

#### • The pre-test function and the post-test function are written in the conftest.py.

#### • The pre-test function sends a get request to the aforementioned endpoint and obtains the result and stores it in a file.

Note:  Since all the tests involves this API's result. Written before the tests start. In the case of API failure, we get to know even before the test starts.



#### • The file 'test_countries_api.py' contains all the 6 tests( 2 tests for each continent specified).

#### • The test involves a csv file that contains the expected value.

Note: The csv file contains several columns like official name, currency etc. In the case, there are multiple values, they are written separated by a comma(,)

#### • The response from the API is considered to be the actual value. The expected value and the actual values are compared.

 Note: The comparison takes place in the function 'check_country_value'. It takes unique country name, obtains the corresponding values from the sheet and the API responses and then compares them togeather.
 Edge cases where the country name argument is not present in the sheet has been added(This includes incorrect country names as well). 

#### • 3 pytest marks("asia", "europe", "africa") has been added to each of the test function to enable continent wise run.

Note: Multiple marks can be added here. Added only region to suit the requirement 

#### • once the tests are run, the post-test function is called. This function clears out the stored API response(cleanup function)

 Though, the API response file is overwritten everytime, there are rare cases where that does happen(Changes in file permissions). This leads to comparison with the older response beating the purpose of the test.

#### • The API endpoint( other constants whichever application) is stored in the 'config.py'

 Constants are more like to change often. having them in a separate file decreases the actual need to change it inside the code. It is also quicker.

### Execution

To execute, please pull the repository into a folder. 

Now, create a venv from the command prompt using the below command.

#### python -m venv venv

This creates a folder called venv that contains the virtual environment. Activate this env by running the /venv/Scripts/activate script.

Once the script is activated, the next step isto install all the libraries which can be done with,

#### pip install -r requirements.txt

Once all the dependencies are installed, execute all the test by running the command 
#### pytest

Execute selective tests by running,
#### pytest -v -m asia -s (for only Asia)

#### pytest -v -q --collect-only -m "asia or africa" -s (for either Asia or Africa)
Similarly, use the mark "europe" to run for Europe.

You should see the output generated in the terminal.
Remove the stdout collector by removing the -s from the above commands. 
Remove the verbose by removing the -v from the above commands

### Notes

The python documentation is added for each of the function.

Comments are added wherever necessary.



