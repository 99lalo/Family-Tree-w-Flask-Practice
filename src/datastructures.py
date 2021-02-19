
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from flask import Flask,jsonify,request
import json

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": 3,
            "first_name": "Veronica",
            "last_name": 'Jackson',
            "age": 20,
            "lucky_numbers": [10,15,31]
            }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        return self._members.append(member)

    def delete_member(self, id):
        for i in range(len(self._members)):
            if  id == self._members[i]["id"]:
                removed = self._members.pop(i)
        return removed

    def get_member(self, id):
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                return self._members[i]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members