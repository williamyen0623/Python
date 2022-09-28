import facebook
graph = facebook.GraphAPI(access_token='EAAGwg103BWkBAP0n2ZAPK26VbOPZCwO2xnK92tV28TlYf5LWI0IEZBAKYmNhytcbnAtlM93RIzajJsh9YooghXf2RvXJNY70EZCdR2VypZCXa7jD2P19ckslyxdZCLlObllaveZB0tAUgwsRAw26a6yYeqqm6C6JHeMZCTG9fO57dTPDxrUPoZCBZCRVoffhPAF62mqkBznzW2eR4WvBa2K4ZCh8pajg6g31oEPgfjyBoSIvennkwn75ZCnZB',version='2.7')

# Post something!
body =  {
    'name':'Post Test',
    'caption': 'Check out this example',
    'description': 'This is a longer description of the attachment',
}
graph.put_wall_post(message='Post Test python graphAPI',attachment=body)

