import pytest
import json
import pandas as pd
import pytest


def read_file():
    """

    This file reads the response from the countries API and returns it in the form of dict

    :return:
    """
    f = open("countries_all.json", "r", encoding='utf-8')
    return json.load(f)


def get_currency_names(currencies):
    """

    The currencies are dynamic and some countries have more than 1.
    This is a simple function to extract the name of all the currenties

    :param currencies: A dict containing all the official currencies
    :return: list of the name of all currencies of the country

    """
    all_currency_names = []
    for each_currency in currencies.keys():
        all_currency_names.append(currencies[each_currency]["name"])
    return all_currency_names


def check_country_value(country_name):
    """
       This function is to compare the data in the csv format with the API response.
       The csv file is considered as the expectation or the truth.
       The API response is considered as the actual result.

       Different fields of the API are compared which are
       common name,
       Official name,
       currency,
       cca2,
       region,
       independence


    :param country_name:
    :return:
    """
    source_country = pd.read_csv("source_countries.csv")
    source_val = source_country.loc[source_country["common"] == country_name]
    response_val = None

    for each_country in read_file():
        if each_country["name"]["common"] == country_name:
            response_val = each_country
            break

    if response_val is None:
        raise ValueError("The common name United Kingdom is not found in the API")

    assert source_val["official"].values[0] == response_val["name"]["official"]
    assert source_val["cca2"].values[0] == response_val["cca2"]
    assert source_val["independent"].values[0] == response_val["independent"]
    assert source_val["currency"].values[0].split(",") == get_currency_names(response_val["currencies"])
    assert source_val["region"].values[0] == response_val["region"]


"""
The below are the test functions where for each country, the API response is evaluated.

"""


@pytest.mark.europe
def test_united_kingdom():

    """
    Added a custom marker europe as to execute the test for those countries alone
    :return:
    """

    check_country_value("United Kingdom")


@pytest.mark.europe
def test_germany():
    """
      Added a custom marker europe as to execute the test for those countries alone
      :return:
      """

    check_country_value("Germany")


@pytest.mark.asia
def test_israel():
    """
      Added a custom marker asia  as to execute the test for those countries alone
      :return:
    """

    check_country_value("Israel")


@pytest.mark.asia
def test_india():

    """
      Added a custom marker asia  as to execute the test for those countries alone
      :return:
    """

    check_country_value("India")


@pytest.mark.africa
def test_lesotho():

    """
      Added a custom marker asia  as to execute the test for those countries alone
      :return:
    """

    check_country_value("Lesotho")


@pytest.mark.africa
def test_djibouti():

    """
      Added a custom marker asia  as to execute the test for those countries alone
      :return:
    """

    check_country_value("Djibouti")
