`brew install jenv`
`echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc`
`echo 'eval "$(jenv init -)"' >> ~/.zshrc`
`jenv versions`
`brew info java`
`jenv add /opt/homebrew/Cellar/openjdk/19.0.2/libexec/openjdk.jdk/Contents/Home`
`brew tap adoptopenjdk/openjdk`
`brew install --cask adoptopenjdk8`
`jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home`
`jenv versions`
`jenv global openjdk64-1.8.0.292`
`java -version`
