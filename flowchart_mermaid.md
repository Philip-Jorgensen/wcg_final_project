flowchart TD
    subgraph gui["Website"]
    start_btn["Start button in GUI"] --> api_connect
    api_connect["Connect to SpectroWorks"] --"Yes"--> get_project["Get project"]
    api_connect --"No"--> Exit

    get_project --> get_items["Get items"]

    get_items --> analyze_test
    start_btn --"Parameters"--> analyze_test["Analayze data"]

    data["Getting data"] --> plot_data["Plot and display data"]
    end
    subgraph api_interface["API Interface"]
    analyze_test --> get_item_data
    get_item_data["Get item data"] --> measurement_number["Check measurement number"]
    measurement_number --"Matches"--> append_values["Append values to list"]
    measurement_number --"Doesn't match"--> skip["Skip item"]
    skip --> get_item_data

    append_values --> more_items["Is there more items left?"]
    more_items --"Yes"-->get_item_data
    more_items --"No"-->remove_outliers_check["Remove outlier parameter set?"]
    remove_outliers_check --"Yes"--> remove_outliers["Remove outliers"]
    remove_outliers_check --"No"--> moving_average_check["Moving average parameter set?"]
    remove_outliers --> moving_average_check
    moving_average_check --"Yes"--> moving_average["Create moving average of data"]
    moving_average_check --"No"--> output_data["Output data"] 
    moving_average --> output_data
    output_data --> data
    end