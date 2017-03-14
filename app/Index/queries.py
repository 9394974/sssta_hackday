from app.Models import Group


def _get_group_basic_info(group):
    group_dict = dict()
    group_dict['group_id'] = group.id
    group_dict['points'] = group.points

    # group first member information
    first_member = group.members.first()
    group_dict['name'] = first_member.name
    group_dict['college'] = first_member.college
    group_dict['grade'] = first_member.grade

    group_dict['qq'] = first_member.qq
    group_dict['phone'] = first_member.phone
    group_dict['email'] = first_member.email

    return group_dict


def get_one_group_information(group_id):
    group = Group.query.get(group_id)
    return _get_group_basic_info(group)


def get_all_group_information():
    groups = Group.query.all()
    groups_list = list()

    for group in groups:
        groups_list.append(_get_group_basic_info(group))

    return groups_list

