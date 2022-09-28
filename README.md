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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
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
- `get` ["/api/users"] ---> Returns all users

- `get` ["/users/:id"] ---> Returns single user i.e Login Route
- `get` ["/api/users/:id"] ---> Returns single user i.e Login Route

- `patch` ["/users/:id"] ---> Updates a single user data i.e Update Route
- `patch` ["/api/users/:id"] ---> Updates a single user data i.e Update Route

- `post` ["/users"] ---> Creates a new user instance i.e Register Route
- `post` ["/api/users"] ---> Creates a new user instance i.e Register Route

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
[Django]: data:image/png;base64,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