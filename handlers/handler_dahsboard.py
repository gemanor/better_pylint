from handlers.mocks import POST, Dashboard, authorizer, db, handler, DELETE, url, errors, Empty


@handler
@POST
@url('/dashboard')
@errors([404, 403])
@authorizer(roles=['all'])
def generate_dashboard(userid):
    data = db.get_dashboard(userid)
    return Dashboard(data)

@handler
@DELETE
@url('/dashboard')
@errors([404, 403])
@authorizer(roles=['reviewers'])
def remove_dashboard(userid):
    data = db.remove_dashboard(userid)
    return Empty(data)
