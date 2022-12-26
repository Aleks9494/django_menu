import os
from django import template
from django.core.exceptions import *
from django_menu.models import MenuItem


register = template.Library()


def get_path_list(context):
    request = context['request']
    current_url = request.path_info
    url_parsed = current_url.split('/')
    url_parsed = list(filter(lambda x: x != "", url_parsed))
    current_item = url_parsed[-1]
    path_list = url_parsed[1:]

    print('cur_url =', current_url)
    print('cur_menu =', current_item)
    print('path_list =', path_list)
    return path_list


@register.inclusion_tag('django_menu/travel_tree.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        root = ""
        chosen_menu_items = get_from_db(menu_name)
        root = build_tree(chosen_menu_items, menu_name)
        context['node'] = root
        print(f"root = {root}")

        cond1 = context['current_menu'] is not None
        cond2 = context['current_menu'] == menu_name

        if cond1 and cond2:
            context['visible_items'] = build_visible_items(root, get_path_list(context))
        else:
            tmp = []
            visible = get_children_names(root, menu_name, tmp)
            visible.append(menu_name)
            context['visible_items'] = visible

        return context

    except ObjectDoesNotExist as e:
        print(e)
        print(f'Menu named \'{menu_name}\' doesn\'t exist!')
        return ''


class TreeItem(object):
    def __init__(self, name, url, parent_name=None, children=None):
        self.name = name
        self.url = url
        self.parent_name = parent_name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, TreeItem)
        self.children.append(node)


def get_from_db(menu_name):
    items_with_menu = MenuItem.objects.select_related('menu')
    chosen_menu_items = [item for item in items_with_menu if item.menu.name == menu_name]
    if not chosen_menu_items:
        raise Exception(f"Menu with name {menu_name} doesn't exist or hasn't items.")
    else:
        return chosen_menu_items


def build_tree(chosen_menu_items, menu_name):
    items_tree = []
    for item in chosen_menu_items:
        if item.parent:
            p = item.parent.name
        else:
            p = menu_name
        items_tree.append(TreeItem(item.name, None, p, None))
    items_tree.append(TreeItem(menu_name, None, None, None))
    root = ""
    root = items_tree[-1]
    for node in items_tree:
        node.children = [i for i in items_tree if i.parent_name == node.name]

    build_urls(root, '/django_menu/', 0)
    return root


def build_urls(node, travel_path, lev):
    next_path = os.path.join(travel_path, node.name)
    node.url = next_path
    print(f'{lev * " "} {node.name} {node.url}')
    if node.children:
        for i in node.children:
            build_urls(i, next_path, lev + 1)


def build_visible_items(root, path_list):
    print(f'root = {root}, path = {path_list}')
    visible_items = []
    visible_items.extend(path_list)
    for item in path_list:
        tmp = []
        get_children_names(root, item, tmp)
        visible_items.extend(tmp)
    print(f"visible items = {visible_items}")
    return visible_items


def get_children_names(root, name_to_find, tmp):
    print(f"root = {root}, name to find = {name_to_find}")
    if name_to_find == root.name:
        if root.children:
            tmp.extend([i.name for i in root.children])
            print('children = ', tmp)
            return tmp
        else:
            return None
    elif root.children:
        for i in root.children:
            get_children_names(i, name_to_find, tmp)
