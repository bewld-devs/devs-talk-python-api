# Dev's Talk API Documentation
### `Author: Beta World Developers`

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://res.cloudinary.com/bewld-devs/image/upload/v1664395344/devs-talk-python-api/devs-no-bg_fong32.png" alt="Logo" width="150" height="100">
  </a>

  <h3 align="center">The Best App For Developers</h3>

  <p align="center">
    Find solutions for all your develpment problems
    <br />
    <a title="Coming soon..." href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a title="Coming soon..." href="#">View Site</a>
    ·
    <a title="Coming soon..." href="#">Report Bug</a>
    ·
    <a title="Coming soon..." href="#">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The API

This API contains confidential user data and should not be publicly available.

Here's why:
* Data Privacy act
* We value client privacy
* Data may contain sensitive information about the client.


Use the `API Documentation` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This API has been built with

[![Django][Django]][Django-url]
<!-- * [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url] -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow this steps carefully to get started with this API.

### Prerequisites

You sould have the following globally available in your machine, if not already installed, use the commands following the prerequisites to install:

#### <b>Python 3</b>

<u><span>`Windows users`</span></u>

  [Download Python](https://www.python.org/downloads/)


<u><span>`Linux users`</span></u>

  ```sh
  $ sudo apt update
  ```

   ```sh
  $ sudo apt install python3
  ```

  #### <b>Visual Studio Code (VS Code)</b>

<u><span>`Windows users`</span></u>

  [Download VS Code](https://code.visualstudio.com/download)


<u><span>`Linux users`</span></u>

  ```sh
  $ sudo apt update
  ```

   ```sh
  $ sudo apt install code
  ```

### Installation

_Follow the below instructions for installations._

1. Open your command prompt/terminal
2. Clone the repo
   ```sh
   git clone https://github.com/bewld-devs/devs-talk-python-api.git
   ```
3. navigate to the cloned folder
   ```sh
    cd devs-talk-python-api
    ```
4. Make a virtual environment
   ```sh
    python -m venv virtual
    ```
5. Activate the virtual environment:

   Windows:
   ```sh
    source virtual/Scripts/activate
    ```
   Linux:
   ```sh
    source virtual/bin/activate
    ```
6. Create environment file

   ```sh
    touch .env
    ```
7. Add required variables inside the .env file
3. Install django packages
   ```sh
   pip install -r requirements
   ```
4. Run Django server
   ```sh
   python3 manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The current working endpoints for this API are.

- `get` ["/"] ---> Home Page: returns greeting

- `get` ["/users"] ---> Returns all users
- `get` ["/api/v1/users"] ---> Returns all users

- `post` ["/dj-rest-auth/login"] ---> Returns single user i.e Login Route
- `post` ["/api/v1/dj-rest-auth/login"] ---> Returns single user i.e Login Route

- `delete` ["/dj-rest-auth/logout"] ---> Logs out a single user ie Logout Route
- `delete` ["/api/v1/dj-rest-auth/logout"] ---> Logs out a single user ie Logout Route

- `patch` ["/dj-rest-auth/password/reset"] ---> Resets a user's password i.e Password Reset Route
- `patch` ["/api/v1/dj-rest-auth/password/reset"] ---> Resets a user's password i.e Password Reset Route

- `patch` ["/dj-rest-auth/password/reset/confirm"] ---> Resets a user's password ie Password Reset Confirm Route
- `patch` ["/api/v1/dj-rest-auth/password/reset/confirm"] ---> Resets a user's password ie Password Reset Confirm Route

- `patch` ["/users/:id"] ---> Updates a single user data i.e Update Route
- `patch` ["/api/users/:id"] ---> Updates a single user data i.e Update Route

- `post` ["/dj-rest-auth/registration"] ---> Creates a new user instance i.e Register Route
- `post` ["/api/v1/dj-rest-auth/registration"] ---> Creates a new user instance i.e Register Route

- `delete` ["/users/:id"] ---> Deletes a user instance i.e Delete Route
- `delete` ["/api/users/:id"] ---> Deletes a user instance i.e Delete Route

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Still in development.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* [Gmail](bewld.devs@gmail.com) - bewld.devs@gmail.com
* [@Twitter](https://twitter.com/bewld-devs) - @bewld-devs
* [LinkedIn](https://linkedin.com/bewld-devs) - bewld-devs

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Django-url]: https://www.djangoproject.com 
[Django]: https://res.cloudinary.com/bewld-devs/image/upload/v1664403505/devs-talk-python-api/django_bzx6gj.png