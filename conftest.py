import os
import requests
import config


def run_api_and_store_result():

    """

    This function uses a GET call to get all the countries from the countries api and stores it in a file.

    """

    try:
        res = requests.get(config.api_url)
        f = open("countries_all.json", "w", encoding="utf-8")
        f.write(res.text)

    except requests.ConnectionError:
        raise ConnectionError("There is a problem with the connection. Please retry after sometime")

    except requests.exceptions.HTTPError as err:
        raise Exception(res.status_code + " " + res.text)

    except requests.exceptions.RequestException as e:
        raise Exception("There has been a request exception. Most likely your connection timedout")


def delete_stored_api_results():

    """

    This function deletes the countries_all.json file that contains the countries API's response
    :return:
    """
    if os.path.exists("countries_all.json"):
        os.remove("countries_all.json")


def pytest_sessionstart(session):

    """
    The pytest_sessionstart function is automatically executed when the session is started. It runs only once and first.
    This function calls the run_api_and_store_result() function.
    No need to pass any manual arguments
    :param session:
    :return:
    """
    run_api_and_store_result()

def pytest_sessionfinish(session, exitstatus):

    """

    This function is automatically executed when the tests are run. It calls delete_stored_api_results.
    No need to pass any manual arguments
    :param session:
    :param exitstatus:
    :return:
    """
    delete_stored_api_results()