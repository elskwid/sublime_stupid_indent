# Stupid Indent for Sublime Text 2

A Sublime Text 2 plugin to determine indentation settings based on filename rather than current indentation.

## Installation
If you're using the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) plugin, you can install the plugin just like any other - `⌘⇧P`, `Install Package`, `Stupid Indent`.

The other way around is to manually clone the repository:

``` bash
# WARNING: This instructions apply only to Mac OS X
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
git clone https://github.com/tzvetkoff/sublime_stupid_indent sublime_stupid_indent
```

## Configuration
Stupid Indent adds settings to the Package Settings menu: `Preferences -> Package Settings -> Stupid Indent`

To customize, just copy `Settings - Default` to `Settings - User` so they aren't overriden during upgrade. Indentations in the User settings take precendence.

The format of each indentation pattern is as follows:

```json
{
    "patterns": ["Gemfile", "*.rb", "*.erb", "*.scss", "*.coffee"],
    "tab_size": 2,
    "translate_tabs_to_spaces": true
}
```

* `patterns` - list of the file patters that are matched against the file name
* `tab_size` - tab size to use for the matched pattern
* `translate_tabs_to_spaces` - translate tabs for the matched pattern

_Note: Settings are modified for the specific file as it is opened._