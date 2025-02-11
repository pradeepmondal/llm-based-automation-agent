tools = [
    {
        "type": "function",
        "function": {
            "name": "generate_data_using_script",
            "description": "Use uv to run a given script with the provided email argument to generate the data files",
            "parameters": {
                "type": "object",
                "properties": {
                    "script_url": {
                        "type": "string",
                        "description": "Script Url"
                    },
                    "email_argument": {
                        "type": "string",
                        "description": "Email argument"
                    },

                },
                "required": ["script_url", "email_argument"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

        {
        "type": "function",
        "function": {
            "name": "format_file",
            "description": "Use prettier with the given version to format the contents of the file whose path is provided",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "File Path"
                    },
                    "prettier_version": {
                        "type": "string",
                        "description": "prettier version"
                    },

                },
                "required": ["file_path", "prettier_version"],
                "additionalProperties": False
            },
            "strict": True
        }
    },


            {
        "type": "function",
        "function": {
            "name": "count_no_of_days",
            "description": "Count the number of a particular day of the week, example Wednesday, from the dates given in a particular file (path specified) and output the result to a given file (path specified)",
            "parameters": {
                "type": "object",
                "properties": {
                    "dates_file_path": {
                        "type": "string",
                        "description": "Path of the file containing the dates"
                    },
                    "day_of_the_week": {
                        "type": "string",
                        "description": "Day of the week as per English calender"
                    },

                    "output_file_path": {
                        "type": "string",
                        "description": "Path of the required output file"
                    },

                },
                "required": ["dates_file_path", "day_of_the_week", "output_file_path"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

                {
        "type": "function",
        "function": {
            "name": "sort_contacts",
            "description": "Sort the array of contacts in a given file (path specified) by prop_1, then by prop_2 and write the result to a output file (path specified)",
            "parameters": {
                "type": "object",
                "properties": {
                    "contacts_file_path": {
                        "type": "string",
                        "description": "Path of the file containing the contacts"
                    },
                    "sorting_properties": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "Property by which the array should be sorted, in the order of priority"
                    },
                    "description": "Array of properties by which the array of contacts should be sorted, in the order of priority"
                },

                    "output_file_path": {
                        "type": "string",
                        "description": "Path of the required output file"
                    },


                },
                "required": ["contacts_file_path", "sorting_properties", "output_file_path"],
                "additionalProperties": False
            },
            "strict": True
        }
    },


    {
        "type": "function",
        "function": {
            "name": "manipulate_logs",
            "description": "Write the first line of the given number of most recent .log file in a given path to a given output file (path specified)",
            "parameters": {
                "type": "object",
                "properties": {
                    "dir_path": {
                        "type": "string",
                        "description": "Path of the directory containing the .log files"
                    },
                    "num_of_recent": {
                        "type": "string",
                        "description": "Required number of most recent .log file"
                    },

                    "output_file_path": {
                        "type": "string",
                        "description": "Path of the required output file"
                    },


                },
                "required": ["dir_path", "num_of_recent", "output_file_path"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

        {
        "type": "function",
        "function": {
            "name": "manipulate_markdowns",
            "description": "Extract the first occurrance of each H1 (line starting with # ) from .md files in a given directory (path specified), then, create a index file in the specified path that that maps each filename to its title ",
            "parameters": {
                "type": "object",
                "properties": {
                    "dir_path": {
                        "type": "string",
                        "description": "Path of the directory containing the .md files"
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path of the required output file"
                    },


                },
                "required": ["dir_path", "output_file_path"],
                "additionalProperties": False
            },
            "strict": True
        }
    },


    {
        "type": "function",
        "function": {
            "name": "extract_email_info",
            "description": "Extract the required information from a email message (path specified) and write it to the specified output file (path specified)",
            "parameters": {
                "type": "object",
                "properties": {
                    "email_file_path": {
                        "type": "string",
                        "description": "Path of the file containing the email message"
                    },
                    "req_info": {
                        "type": "string",
                        "description": "The required information eg: email address, name, etc."
                    },

                    "output_file_path": {
                        "type": "string",
                        "description": "Path of the required output file"
                    },

                },
                "required": ["email_file_path", "req_info", "output_file_path"],
                "additionalProperties": False
            },
            "strict": True
        }
    },





    ########## Starting Business Tools Description ###############

    # Tool Description for task B3 - Fetch data from an API and save it
        {
        "type": "function",
        "function": {
            "name": "fetch_and_save_data",
            "description": "Fetch data from the given api url with optional parameters and save to the specified output file",
            "parameters": {
                "type": "object",
                "properties": {
                    "api_url": {
                        "type": "string",
                        "description": "Url of the api endpoint"
                    },
                    "params": {
                        "type": "string",
                        "description": "Parameters for the api call"
                    },

                    "output_file_path": {
                        "type": "string",
                        "description": "Path of the required output file"
                    },

                },
                "required": ["api_url", "output_file_path"],
                "additionalProperties": False
            },
            "strict": False
        }
    },

    {
        "type": "function",
        "function": {
            "name": "clone_and_commit_git_repo",
            "description": "This function handles prompts that involve cloning a git repository. It takes the entire prompt and processes it to clone the repo and commit changes.",
            "parameters": {
            "type": "object",
            "properties": {
                "prompt": {
                "type": "string",
                "description": "The entire user prompt that asks for cloning a git repository."
                }
            },
            "required": ["prompt"],
            "additionalProperties": False
            },
            "strict": True
        }
            },
    
]