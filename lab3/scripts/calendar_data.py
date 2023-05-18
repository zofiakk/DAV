"""Calendar data

This script is used to create csv file with the academic calendar data
as well as read it to the DataFRame and create and calculate values
of a necessary additional columns 

This file contains the following function:

    * save_calendar_data - creates the csv file with the dates
    * add_to_calendar_data- returns DataFRame withe the academic calendar data
"""
import pandas as pd


def save_calendar_data(file_name: str):
    """Create the Dataframe with the necessary data and
    save it to csv file

    :param file_name: Name of the output csv file
    :type file_name: str
    """
    data = pd.DataFrame({'task': ['Classes', 'Language exams', 'Exams', 'Mid-sem Breaks',
                                  'Individual decisions', 'Linkages',  'Resignation',
                                  'Mid-term break'],
                         'start_1_winter': pd.to_datetime(['2 Oct 2023', '29 Jan 2024',
                                                           '29 Jan 2024', '22 Dec 2023',
                                                           '4 Mar 2024', None,
                                                           '19 Jan 2024', None]),
                         'end_1_winter': pd.to_datetime(['21 Dec 2023',  '30 Jan 2024',
                                                         '11 Feb 2024', '7 Jan 2024',
                                                         '31 Mar 2024', None,
                                                         '19 Jan 2024', None]),
                         'start_2_winter': pd.to_datetime(['8 Jan 2024', '24 Feb 2024',
                                                           '19 Feb 2024', None, None,
                                                           '1 Oct 2023', '20 Oct 2023',
                                                           None]),
                         'end_2_winter': pd.to_datetime(['28 Jan 2024', '24 Feb 2024',
                                                         '25 Feb 2024', None, None,
                                                         '18 Feb 2024', '20 Oct 2023',
                                                         None]),
                         'start_1_summer': pd.to_datetime(['26 Feb 2024', '17 Jun 2024',
                                                           '17 Jun 2024', '28 Mar 2024',
                                                           '16 Sep 2024', None,
                                                           '1 Jul 2024', None]),
                         'end_1_summer': pd.to_datetime(['16 Jun 2024', '18 Jun 2024', '7 Jul 2024',
                                                         '2 Apr 2024', '30 Sep 2024', None,
                                                         '1 Jul 2024', None]),
                         'start_2_summer': pd.to_datetime([None, '2 Sep 2024', '2 Sep 2024',
                                                           '8 Jul 2024', None, '1 Jun 2024',
                                                           '15 Mar 2024', None]),
                         'end_2_summer': pd.to_datetime([None, '3 Sep 2024', '15 Sep 2024',
                                                         '30 Sep 2024', None, '30 Sep 2024',
                                                         '15 Mar 2024', None]),
                         'start_none': pd.to_datetime([None, None, None, None, None, None, None,
                                                       '12 Feb 2024', ]),
                         'end_none': pd.to_datetime([None, None, None, None, None, None, None,
                                                     '18 Feb 2024']),
                         'name_1_winter': ['Classes', 'Language exams', 'Exams',  'Mid-sem breaks',
                                           'Individual decisions', 'Linkage deletions',
                                           'Course resignation', 'Mid-term break'],
                         'name_2_winter': ['Classes', 'Language exams', 'Make-up exams',
                                           'Mid-sem breaks', 'Individual decisions',
                                           'Linkage requests', 'Linkage resignation',
                                           'Mid-term break'],
                         'name_1_summer': ['Classes', 'Language exams', 'Exams', 'Mid-sem breaks',
                                           'Individual decisions', 'Linkage deletions',
                                           'Course resignation', 'Mid-term break'],
                         'name_2_summer': ['Classes', 'Language exams', 'Make-up exams', 'Holidays',
                                           'Individual decisions', 'Linkage requests',
                                           'Linkage resignation', 'Mid-term break']})
    # Save to the file
    data.to_csv(file_name, index=False)


def add_to_calendar_data(file_name: str) -> pd.DataFrame:
    """Function which reads and adds additional columns to the
    DataFrame withe the academic calendar dates

    :param file_name: Nae of the csv file with the dates
    :type file_name: str
    :return: DataFrame with the data
    :rtype: pd.DataFrame
    """
    # Read the csv file
    data = pd.read_csv(file_name, sep=",", infer_datetime_format=True)
    cols = data.columns[1:11]
    data[cols] = data[cols].apply(
        pd.to_datetime, errors='coerce', format='%Y-%m-%d')

    # Calculate duration of each task and the days to its beginning and end
    for i in [1, 2]:
        suffix = '_' + str(i)
        data['days_to_start' + suffix + "_winter"] = (data['start' + suffix + "_winter"]
                                                      - min(data['start_1_winter'].min(),
                                                            data['start_2_winter'].min())).dt.days
        data['days_to_end' + suffix + "_winter"] = (data['end' + suffix + "_winter"] -
                                                    min(data['start_1_winter'].min(),
                                                        data['start_2_winter'].min())).dt.days
        data['task_duration' + suffix + "_winter"] = (data['days_to_end' + suffix + "_winter"]
                                                      - data['days_to_start' + suffix
                                                             + "_winter"] + 1)
        data['days_to_start' + suffix + "_summer"] = (data['start' + suffix + "_summer"]
                                                      - min(data['start_1_winter'].min(),
                                                            data['start_2_winter'].min())).dt.days
        data['days_to_end' + suffix + "_summer"] = (data['end' + suffix + "_summer"]
                                                    - min(data['start_1_winter'].min(),
                                                          data['start_2_winter'].min())).dt.days
        data['task_duration' + suffix + "_summer"] = (data['days_to_end' + suffix + "_summer"]
                                                      - data['days_to_start' + suffix
                                                             + "_summer"] + 1)

    data['days_to_start_none'] = (data['start_none'] - min(data['start_1_winter'].min(),
                                                           data['start_2_winter'].min())).dt.days
    data['days_to_end_none'] = (data['end_none'] - min(data['start_1_winter'].min(),
                                                       data['start_2_winter'].min())).dt.days
    data['task_duration_none'] = data['days_to_end_none'] - \
        data['days_to_start_none'] + 1
    return data
