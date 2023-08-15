from django.shortcuts import redirect, render
from django.contrib import messages

def config_env_file(request):
  # List all enviroment variable
  list_env_variable = ['OPENAI_API_KEY', 'SF_USER', 'SF_PASSWD', 'SF_CLIENT_ID', 'SF_CLIENT_SECRET', 'SF_AUTH_URL', 
                       'POSTGRE_USER', 'POSTGRE_PASSWD', 'POSTGRE_HOST', 'POSTGRE_PORT', 'POSTGRE_DATABASE']

  # Read all enviroment variable and send to context in html
  current_env_variable  = {}
  with open('.env', 'r') as file:
    for env_variable in file:
      key, value = env_variable.strip().split('=', 1)
      current_env_variable[key] = value

  # Save all data when submit button
  new_env_variable = []
  if request.method == 'POST':
    for env in list_env_variable :
      variable = request.POST.get(env)
      if variable != None:
        new_env_variable.append(f"{env}={variable}") 
      else: 
        new_env_variable.append(f"{env}={current_env_variable[env]}")

    try:
      # Convert list to dict
      array_as_dict = dict(item.split('=') for item in new_env_variable)

      if current_env_variable == array_as_dict:
        # print("Hai kiểu dữ liệu giống nhau.")
        # Notification wanning
        messages.success(request, 'No change data!')
      else:
        # Notification success and write data in .env file
        # print("Hai kiểu dữ liệu khác nhau.")
        messages.success(request, 'Edit data successful!')

        # Write data to .env file
        with open('.env', 'w') as file:
          for env  in new_env_variable :
            file.writelines(env + '\n')

      
    except ZeroDivisionError:
      # Notification error
      messages.error(request, 'Edit data error!')
    return redirect('/management/config')

  else:
    return render(request, 'index.html', context= current_env_variable)
