class FilterSubjects(object):

    def blank_space(list):

        while '' in list:

            list.remove('')

        return list

    def remove_word_event_note(list):

        while 'event_note' in list:

            list.remove('event_note')

        return list

    def remove_hours(list):

        list = [aux for aux in list if "h" not in aux]

        return list

    def remove_letter_a(list):

        list_codes = [aux for aux in list if "A" not in aux]

        return list_codes

    def remove_letter_o(list):

        list_codes = [aux for aux in list if "O" not in aux]

        return list_codes

    def remove_vogals(list):

        list_A = FilterSubjects.remove_letter_a(list)
        list_final = FilterSubjects.remove_letter_o(list_A)

        return list_final

    def remove_cod_of_list_name(list_code,list):

        list_names = [x for x in list if not any(ignore in x for ignore in list_code)]

        return list_names

    def remove_accents(list_names):

        list_names = [x.replace('Á', 'A') for x in list_names]
        list_names = [x.replace('À', 'A') for x in list_names]
        list_names = [x.replace('Â', 'A') for x in list_names]
        list_names = [x.replace('Ã', 'A') for x in list_names]
        list_names = [x.replace('É', 'E') for x in list_names]
        list_names = [x.replace('Ê', 'E') for x in list_names]
        list_names = [x.replace('Í', 'I') for x in list_names]
        list_names = [x.replace('Õ', 'O') for x in list_names]
        list_names = [x.replace('Ô', 'O') for x in list_names]
        list_names = [x.replace('Ó', 'O') for x in list_names]
        list_names = [x.replace('Ç', 'C') for x in list_names]

        return list_names