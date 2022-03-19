from project.team import Team
import unittest


class TeamTests(unittest.TestCase):

    def setUp(self) -> None:
        self.team = Team('Avengers')

    def test_init(self):
        error_message = "Team Name can contain only letters!"
        wrong_name = '123'
        with self.assertRaises(ValueError) as context:
            self.team = Team(wrong_name)
        self.assertEqual(error_message, str(context.exception))

        team_name = 'AvengersExpanded'
        self.team.name = team_name
        self.assertEqual(team_name, self.team.name)
        self.assertTrue(hasattr(self.team, '_Team__name'))
        self.assertEqual(team_name, self.team._Team__name)

        expected_members = {}
        self.assertDictEqual(expected_members, self.team.members)

    def test_getter_setter_validation(self):
        team_name = 'Avengers'
        self.team = Team(team_name)

        wrong_name = 'The_Avengers'
        error_message = "Team Name can contain only letters!"

        with self.assertRaises(ValueError) as contex:
            self.team.name = wrong_name
        self.assertEqual(error_message, str(contex.exception))

        self.assertEqual(team_name, self.team.name)

    def test_add_member_method(self):
        new_members = {'Hulk': 38, 'Thor': 242, 'Peter Parker': 'too young'}
        retval = self.team.add_member(**new_members)
        self.assertEqual('Successfully added: Hulk, Thor, Peter Parker', retval)
        self.assertDictEqual(new_members, self.team.members)

        add_members = {'Steve': 105, 'Peter Parker': 18}
        retval = self.team.add_member(**add_members)
        self.assertEqual('Successfully added: Steve', retval)

        expected_members = {'Hulk': 38, 'Thor': 242, 'Peter Parker': 'too young', 'Steve': 105}
        self.assertDictEqual(expected_members, self.team.members)

    def test_remove_member_successful(self):
        name = 'Peter Parker'
        message_on_success = f"Member {name} removed"
        new_members = {'Hulk': 38, 'Thor': 242, 'Peter Parker': 'too young'}

        self.team.add_member(**new_members)

        retval = self.team.remove_member(name)
        self.assertEqual(message_on_success, retval)

        expected_members = {'Hulk': 38, 'Thor': 242}
        self.assertDictEqual(expected_members, self.team.members)

    def test_remove_member_unsuccessful(self):
        name = 'Peter Parker'
        new_members = {'Hulk': 38, 'Thor': 242}
        message_on_failure = f"Member with name {name} does not exist"

        self.team.add_member(**new_members)
        retval = self.team.remove_member(name)
        self.assertEqual(message_on_failure, retval)

    def test_dunder_greater_true(self):
        members = {'Hulk': 38, 'Thor': 242, 'Peter Parker': 'too young'}
        self.team.add_member(**members)

        other_team = Team('Hydra')
        other_members = {'Bucky': 106, 'Red Skull': 45}
        other_team.add_member(**other_members)

        expected = True
        self.assertEqual(expected, self.team > other_team)

    def test_dunder_greater_false(self):
        members = {'Hulk': 38, 'Thor': 242}
        self.team.add_member(**members)

        other_team = Team('Hydra')
        other_members = {'Bucky': 106, 'Red Skull': 45, 'Pierce': 60}
        other_team.add_member(**other_members)

        expected = False
        self.assertEqual(expected, self.team > other_team)

    def test_dunder_len(self):
        members = {'Hulk': 38, 'Thor': 242}
        self.team.add_member(**members)
        expected = 2
        self.assertEqual(expected, len(self.team))

    def test_dunder_add(self):
        members = {'Hulk': 38, 'Thor': 242}
        self.team.add_member(**members)
        other_members = {'Bucky': 106, 'Red Skull': 45, 'Pierce': 60}
        other_team = Team("Hydra")
        other_team.add_member(**other_members)

        mcu_team = self.team + other_team
        test_team = Team('Test')
        test_team.add_member(**self.team.members)
        test_team.add_member(**other_team.members)

        expected_name = self.team.name + other_team.name
        self.assertEqual(expected_name, mcu_team.name)
        self.assertDictEqual(test_team.members, mcu_team.members)

    def test_dunder_str(self):
        members = {'Hulk': 38, 'Thor': 242, 'Peter Parker': 18}
        self.team.add_member(**members)

        result = [f"Team name: {self.team.name}"]
        members = list(sorted(self.team.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        retval = "\n".join(result)
        self.assertEqual(str(self.team), retval)


if __name__ == '__main__':
    unittest.main()
