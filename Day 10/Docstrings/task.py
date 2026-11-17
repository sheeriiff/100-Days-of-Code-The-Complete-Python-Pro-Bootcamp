def format_name(f_name, l_name):
    """I am writing a docstring for my function:
    take the first and last name, formate it and return the title case version """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



