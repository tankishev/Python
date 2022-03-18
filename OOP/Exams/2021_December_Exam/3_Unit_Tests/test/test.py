from project.team import Team
import unittest


class TeamTests(unittest.TestCase):

    def setUp(self) -> None:
        self.t = Team('TeamName')
        new_members = {'Valio': 22, 'Pesho': 42}
        self.t.add_member(**new_members)
        self.t.remove_member('Valio')
        self.assertTrue(hasattr(self.t, '_Team__name'))
        self.assertDictEqual(self.t.members, {'Pesho': 42})
        self.assertEqual(self.t.name, 'TeamName')

    def test_getter_setter_validation(self):
        new_team = "Avengers123._"
        with self.assertRaises(ValueError) as contex:
            Team(new_team)
        self.assertEqual("Team Name can contain only letters!", str(contex.exception))
        self.assertEqual(self.t.name, 'TeamName')

    def test_add_member_method(self):
        new_members = {'Pesho': 32, 'Bobi': 32, 'Nicki': 88}
        retval = self.t.add_member(**new_members)
        self.assertEqual(retval, 'Successfully added: Bobi, Nicki')
        self.assertDictEqual(self.t.members, {'Pesho': 42, 'Bobi': 32, 'Nicki': 88})

    def test_remove_member_method(self):
        retval_not_existing = self.t.remove_member('Misho')
        retval_ok = self.t.remove_member('Pesho')
        self.assertDictEqual({}, self.t.members)
        self.assertEqual('Member with name Misho does not exist', retval_not_existing)
        self.assertEqual('Member Pesho removed', retval_ok)

    def test_dunder_greater(self):
        other = Team('Other')
        other_members = {'Jess': 10, 'Stefan': 20}
        other.add_member(**other_members)
        self.assertFalse(self.t > other)
        self.assertTrue(self.t < other)
        other.remove_member('Jess')
        self.assertFalse(self.t > other)
        self.assertFalse(self.t < other)
        other.remove_member('Stefan')
        self.assertTrue(self.t > other)
        self.assertFalse(self.t < other)

    def test_dunder_len(self):
        self.assertTrue(len(self.t) == len(self.t.members))
        self.assertEqual(len(self.t), 1)

    def test_dunder_add(self):
        other_members = {'Viki': 12, 'Bobi': 32}
        other_t = Team('Other')
        other_t.add_member(**other_members)
        new_team = self.t + other_t
        self.assertEqual(new_team.name, 'TeamNameOther')
        self.assertDictEqual(new_team.members, {'Pesho': 42, 'Viki': 12, 'Bobi': 32})

    def test_dunder_str(self):
        new_members = {'Viki': 12, 'Bobi': 32}
        self.t.add_member(**new_members)
        result = [f"Team name: {self.t.name}"]
        members = list(sorted(self.t.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        retval = "\n".join(result)
        self.assertEqual(str(self.t), retval)


if __name__ == '__main__':
    unittest.main()
