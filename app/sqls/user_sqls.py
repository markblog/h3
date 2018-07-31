get_users_except_current_user = """
SELECT id, name FROM public.user
WHERE group_id = :group_id AND id <> :user_id
ORDER BY name ASC
"""