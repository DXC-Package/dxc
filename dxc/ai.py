def convert(my_name):
    """
    Print a line about converting a notebook.
    Args:
        my_name (str): person's name
    Returns:
        None
    """

    print(f"I'll convert a notebook for you some day, {my_name}.")

def read_data_frame_from_remote_json(json_url):
    with urllib.request.urlopen(json_url) as url:
        json_data = json.loads(url.read().decode())
    df = flatten_json_into_dataframe(json_data)
    return(df)

