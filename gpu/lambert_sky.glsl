#version 330

// Input vertex attributes (from vertex shader)
in vec2 fragTexCoord;
// in vec4 fragColor;

uniform vec2 mouse;

// Output fragment color
out vec4 finalColor;

// vec2 screenSize = vec2(320, 180);

const int radius = 65536;


vec3 albedo = vec3(36, 172, 226);
float intensity = 0.003;
float ambient = 0.001;

void main() {
    vec3 light = normalize(vec3( (mouse.x - 600) / 600, (-mouse.y + 400) / 400, 1 ));

    vec2 pos = vec2(gl_FragCoord.x - 600, gl_FragCoord.y - 400);

    float z = sqrt( -(pos.x*pos.x) -(pos.y*pos.y) + 65536 );

    vec3 normal = normalize(vec3(pos.x, pos.y, z));
    normal.z = z / 256;

    float v = dot(normal, light);

    vec3 material = albedo * v * intensity + ambient * albedo;

    finalColor = vec4(material, 255);
}