from django.shortcuts import redirect, render
  
def get_home(request):
  # Mesage notification
  message = ''

  # List all enviroment variable
  list_env_variable = ['OPENAI_API_KEY', 'SF_USER', 'SF_PASSWD', 'SF_CLIENT_ID', 'SF_CLIENT_SECRET', 'SF_AUTH_URL', 
                       'POSTGRE_USER', 'POSTGRE_PASSWD', 'POSTGRE_HOST', 'POSTGRE_PORT', 'POSTGRE_DATABASE']

  # Read all enviroment variable and send to context in html
  current_env_variable  = {}
  with open('.env', 'r') as file:
    for env_variable in file:
      print('')
      key, value = env_variable.strip().split('=', 1)
      current_env_variable[key] = value

  # print('1')
  # print(current_env_variable)
  # Save all data when change in input
  new_env_variable = []
  if request.method == 'POST':
    for env in list_env_variable :
      variable = request.POST.get(env)
      new_env_variable.append(f"{env}={variable}") if variable != None else new_env_variable.append(f"{env}={current_env_variable[env]}")
      
    # Write data to .env file
    try:
      with open('.env', 'w') as file:
        for env  in new_env_variable :
          file.writelines(env + '\n')
      print('2')
      print(current_env_variable)
      message = 'Edit data successful!'
    except ZeroDivisionError:
      message = "Edit data error!"
    return redirect('/')

  else:
    return render(request, 'index.html', context= current_env_variable)
