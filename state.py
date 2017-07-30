# state.py

#%%
from state_machine import State, acts_as_state_machine, before, after, Event, InvalidStateTransition


@acts_as_state_machine
class Process:
    created = State(initial=True)
    running = State()
    terminated = State()

    run = Event(from_states=created, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)

    def __init__(self, name):
        self.name = name

    @after('run')    
    def run_info(self):
        print(f'{self.name} is running')

    @before('terminate')
    def terminate_info(self):
        print(f'{self.name} terminated')

p = Process('Test')
p.current_state
p.run()
p.terminate()
    