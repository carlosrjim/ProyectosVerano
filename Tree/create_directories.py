import os

# Dictionary mapping frameworks to their respective languages
framework_map = {
    'Laravel': 'php',
    'Symfony': 'php',
    'CodeIgniter': 'php',
    'Yii': 'php',
    'Zend Framework (Laminas)': 'php',
    'Phalcon': 'php',
    'CakePHP': 'php',
    'Slim': 'php',
    'FuelPHP': 'php',
    'Laminas': 'php',
    'Django': 'python',
    'Flask': 'python',
    'FastAPI': 'python',
    'Pyramid': 'python',
    'Tornado': 'python',
    'Bottle': 'python',
    'Falcon': 'python',
    'CherryPy': 'python',
    'Hug': 'python',
    'Dash': 'python',
    'React': 'javascript',
    'Angular': 'javascript',
    'Vue.js': 'javascript',
    'Svelte': 'javascript',
    'Next.js': 'javascript',
    'Nuxt.js': 'javascript',
    'Express.js': 'javascript',
    'NestJS': 'typescript',
    'Meteor': 'javascript',
    'Electron': 'javascript',
    'Spring Boot': 'java',
    'Hibernate': 'java',
    'Struts': 'java',
    'JavaServer Faces (JSF)': 'java',
    'Vaadin': 'java',
    'Play Framework': 'java',
    'Dropwizard': 'java',
    'Micronaut': 'java',
    'Grails': 'java',
    'Spark': 'java',
    'ASP.NET Core': 'csharp',
    'Blazor': 'csharp',
    'NancyFX': 'csharp',
    'Umbraco': 'csharp',
    'DotVVM': 'csharp',
    'Orchard Core': 'csharp',
    'MonoGame': 'csharp',
    'IdentityServer': 'csharp',
    'OpenRA': 'csharp',
    'ServiceStack': 'csharp',
    'Qt': 'cpp',
    'Boost': 'cpp',
    'Cinder': 'cpp',
    'JUCE': 'cpp',
    'Poco C++': 'cpp',
    'wxWidgets': 'cpp',
    'Ogre3D': 'cpp',
    'SFML': 'cpp',
    'GTKmm': 'cpp',
    'VCL (Embarcadero)': 'cpp',
    'Gin': 'go',
    'Echo': 'go',
    'Beego': 'go',
    'Revel': 'go',
    'Fiber': 'go',
    'Buffalo': 'go',
    'Goji': 'go',
    'Martini': 'go',
    'Iris': 'go',
    'Chi': 'go',
    'Vapor': 'swift',
    'Kitura': 'swift',
    'Perfect': 'swift',
    'SwiftNIO': 'swift',
    'Zewo': 'swift',
    'SwiftKuery': 'swift',
    'IBM Cloud': 'swift',
    'Plotly': 'swift',
    'SwiftData': 'swift',
    'Alchemy': 'swift',
    'Ktor': 'kotlin',
    'Vert.x': 'kotlin',
    'Javalin': 'kotlin',
    'Exposed': 'kotlin',
    'TornadoFX': 'kotlin',
    'Koin': 'kotlin',
    'Kotest': 'kotlin',
    'Arrow': 'kotlin',
    'Moshi': 'kotlin',
    'Micronaut': 'kotlin',
    'Rocket': 'rust',
    'Actix': 'rust',
    'Tide': 'rust',
    'Yew': 'rust',
    'Tonic': 'rust',
    'Axum': 'rust',
    'Warp': 'rust',
    'Gotham': 'rust',
    'Nickel': 'rust',
    'Conrod': 'rust',
    'Yesod': 'haskell',
    'Snap': 'haskell',
    'Scotty': 'haskell',
    'Servant': 'haskell',
    'Spock': 'haskell',
    'Happstack': 'haskell',
    'Reflex': 'haskell',
    'Hakyll': 'haskell',
    'Groundhog': 'haskell',
    'Heist': 'haskell',
    'Ruby on Rails': 'ruby',
    'Sinatra': 'ruby',
    'Hanami': 'ruby',
    'Grape': 'ruby',
    'Padrino': 'ruby',
    'Volt': 'ruby',
    'Cuba': 'ruby',
    'Ramaze': 'ruby',
    'Camping': 'ruby',
    'Roda': 'ruby',
    'Phoenix': 'elixir',
    'Nerves': 'elixir',
    'Plug': 'elixir',
    'Ecto': 'elixir',
    'Absinthe': 'elixir',
    'Cowboy': 'elixir',
    'Broadway': 'elixir',
    'Tonic': 'elixir',
    'Scenic': 'elixir',
    'ExDoc': 'elixir',
    'Catalyst': 'perl',
    'Dancer': 'perl',
    'Mojolicious': 'perl',
    'Mason': 'perl',
    'PerlDancer2': 'perl',
    'Plack': 'perl',
    'Jifty': 'perl',
    'Maypole': 'perl',
    'Amon2': 'perl',
    'Tatsumaki': 'perl',
    'OpenResty': 'lua',
    'Lapis': 'lua',
    'Sailor': 'lua',
    'Orbit': 'lua',
    'Kepler': 'lua',
    'WSAPI': 'lua',
    'Pegasus': 'lua',
    'ETlua': 'lua',
    'Fengari': 'lua',
    'MoonScript': 'lua',
    'Flutter': 'dart',
    'Aqueduct': 'dart',
    'Angel': 'dart',
    'Jaguar': 'dart',
    'Shelf': 'dart',
    'Alfred': 'dart',
    'Conduit': 'dart',
    'Redstone': 'dart',
    'Dart Frog': 'dart',
    'Mison': 'dart',
    'Cocoa Touch': 'objective-c',
    'AppKit': 'objective-c',
    'Core Data': 'objective-c',
    'AFNetworking': 'objective-c',
    'Mantle': 'objective-c',
    'RestKit': 'objective-c',
    'MagicalRecord': 'objective-c',
    'ReactiveObjC': 'objective-c',
    'UIKit': 'objective-c',
    'Foundation': 'objective-c',
    # Add more frameworks and languages as needed
}

# Function to create directory structure
def create_directories(course_file):
    with open(course_file, 'r') as file:
        for line in file:
            course = line.strip()
            language = framework_map.get(course, course.lower())
            if not os.path.exists(language):
                os.makedirs(language)
            course_path = os.path.join(language, course.lower())
            if not os.path.exists(course_path):
                os.makedirs(course_path)

if __name__ == '__main__':
    create_directories('cursos.txt')