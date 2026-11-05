# Languages

English and Spanish are included. The text covers notifications, prompts, the radio chatter, the Bond & Counsel screen and the paperwork screen.

{% stepper %}
{% step %}
### Copy a locale

Copy `locales/en.lua` to `locales/xx.lua`.
{% endstep %}

{% step %}
### Translate

Change `Locales['en']` to `Locales['xx']` and translate the strings. Keep the `%s` placeholders.
{% endstep %}

{% step %}
### Switch to it

Set `Config.Locale = 'xx'`.
{% endstep %}
{% endstepper %}
