import yaml


# This is going to translate the tint format for this online tool:
# https://turingmachinesimulator.com/
def translate_tint_to_the_online_tm_format(name):
    machine = None
    with open(name, 'r') as stream:
        try:
            machine = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    direction_translations = {'L': '<', 'R': '>', 'S': '-'}

    start = machine.get('start')
    accept = machine.get('accept')
    new_transitions = []
    for i in machine.get('transitions'):
        current_state = i[0]
        read_symbol = i[1]
        new_state = i[2]
        write_symbol = i[3]
        direction = direction_translations[i[4]]
        new_transitions.append(f"{current_state},{read_symbol}\n{new_state},{write_symbol},{direction}\n\n")

    final = f"name: {name}\ninit: {start}\naccept: {accept} \n{str().join(new_transitions)}"

    with open(f"converted-{name}", 'w') as output:
        output.write(final)


if __name__ == '__main__':
    translate_tint_to_the_online_tm_format("q6.yaml")
