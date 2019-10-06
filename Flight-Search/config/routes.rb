Rails.application.routes.draw do
  get 'flight/index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  root 'flight#index'
end
