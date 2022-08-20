def get_all_from_database(modal_object):
    """Get all objects for model from table in database."""
    return modal_object.objects.all()
    
