def get_target_summary(target):
    """
    Returns a simple placeholder summary for a target gene.
    """

    return {
        "target": target,
        "status": "Placeholder",
        "message": f"{target} lookup has not been implemented yet."
    }